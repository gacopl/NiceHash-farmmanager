#!/bin/sh
#
# DON'T EDIT THIS FILE DIRECTLY!
#
# Instead, create your own configuration by setting any of the 7 variables
# listed below in /etc/default/nhmfm. For example: adding NH_USER=noob
# to /etc/default/nhmfm makes the service run under the 'noob' account,
# overruling the default value of 'nhmfm'.
#
# Accepted variables with default values -if any- in parentheses:
# NH_USER	# username to run nhmfm under (nhmfm)
# NH_HOME	# directory of nhmfm.py (/opt/nhmfm)
# NH_DATA	# directory of nhmfm's db, cache and logs (/var/opt/nhmfm)
# NH_PIDFILE	# full path of nhmfm.pid (/var/run/nhmfm/nhmfm.pid)
# PYTHON_BIN	# full path of the python binary (/usr/bin/python)
# NH_OPTS	# extra cli options for nhmfm, see 'nhmfm.py --help'
# SSD_OPTS	# extra options for start-stop-daemon, see 'man start-stop-daemon'

### BEGIN INIT INFO
# Provides:          nhmfm
# Required-Start:    $network $remote_fs
# Required-Stop:     $network $remote_fs
# Should-Start:      $named deluged network-manager nzbget qbittorrent-nox sabnzbdplus transmission-daemon
# Should-Stop:       $named deluged network-manager nzbget qbittorrent-nox sabnzbdplus transmission-daemon
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: nhmfm PVR for Usenet and torrents
# Description:       starts instance of nhmfm using start-stop-daemon
### END INIT INFO

DESC=nhmfm
CONFIG=/etc/default/nhmfm

# don't accept config vars from the shell environment
unset NH_USER NH_HOME NH_DATA NH_PIDFILE PYTHON_BIN NH_OPTS SSD_OPTS

# source lsb init functions
. /lib/lsb/init-functions

# try loading the configuration file
[ -r "$CONFIG" ] && . "$CONFIG" \
	|| log_action_msg "$DESC: $CONFIG unreadable, falling back to default settings"

# assorted settings and their defaults
: "${NH_USER:=nhmfm}"
: "${NH_HOME:=/opt/nhmfm}"
: "${NH_DATA:=/opt/nhmfm}"
: "${NH_PIDFILE:=/var/run/nhmfm/nhmfm.pid}"
: "${PYTHON_BIN:=/usr/bin/python3}"

# basic sanity checks
([ -x "$PYTHON_BIN" ] && [ -f "$NH_HOME/nhmfm.py" ]) || {
	log_failure_msg "$DESC: init script setup failed basic sanity checks, aborting!";
	# exit zero since this condition may also occur after a user
	# uninstalled NH while leaving this script in place.
	exit 0;
}

start_NH() {
	# create directories with sensible ownership and permissions
	# (but refuse to touch any pre-existing ones)
	for D in "$(dirname "$NH_PIDFILE")" "$NH_DATA"; do
		[ ! -d "$D" ] && {
			install --directory --owner="$NH_USER" --group=root --mode=0750 "$D" || exit 1;
		}
	done

	log_daemon_msg "Starting $DESC"
	start-stop-daemon --start --quiet --background --pidfile "$NH_PIDFILE" --make-pidfile --chdir "$NH_HOME" --chuid "$NH_USER" --oknodo --exec "$PYTHON_BIN" $SSD_OPTS -- \
		nhmfm.py --daemon --quiet --pid_file="$NH_PIDFILE" --data_dir="$NH_DATA" $NH_OPTS
	log_end_msg $? || exit $?
}

stop_NH() {
	log_daemon_msg "Stopping $DESC"
	# for security reasons, require the process to be both:
	# 1) listed in the pidfile and 2) running as $NH_USER
	start-stop-daemon --stop --quiet --pidfile "$NH_PIDFILE" --user "$NH_USER" --retry 15 --oknodo
	log_end_msg $? || exit $?
}

case "$1" in
	start)
		start_NH;;
	stop)
		stop_NH;;
	restart|force-reload)
		stop_NH && start_NH;;
	status)
		status_of_proc -p "$NH_PIDFILE" "$PYTHON_BIN" "$DESC"
		exit $?;;
	*)
		echo "Usage: $0 {start|stop|restart|force-reload|status}" >&2
		exit 3;;
esac

exit 0
