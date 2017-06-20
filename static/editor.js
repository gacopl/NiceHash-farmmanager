function test() {
    var rigs = [];

$("table#rigs tr").each(function() {
    var arrayOfThisRow = [];
    var tableData = $(this).find('td');
    if (tableData.length > 0) {
        tableData.each(function() { arrayOfThisRow.push($(this).find('input[type="text"]').val()); });
        rigs.push(arrayOfThisRow);
    }
});
console.log(rigs)

$.ajax({
   type: "POST",
   data: {rigs:rigs},
   traditional: true,
   url: "setRigs",
   success: function(msg){
     $('.answer').html(msg);
   }
});
window.location.href = '/nhmfm'
}

function add() {
    $('#rigs tr:last').after('<tr><td><input type=text value=""></td><td><input type=text value=""></td><td><input type=text value=""></td><td><input type=text value=""></td><td><input type=button value="Delete" onclick="$(this).closest(\'tr\').remove();"></td></tr>');
}

