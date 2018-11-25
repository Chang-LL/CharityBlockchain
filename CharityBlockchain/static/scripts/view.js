$('#donate').hide();
$('#record').hide();
$('#foundation').hide();
$('#hu').click(function () {
    $('#donate').hide();
    $('#record').hide();
    $('#foundation').hide();
    $('#usermessage').show();
});
$('#hd').click(function () {
    $('#usermessage').hide();
    $('#record').hide();
    $('#foundation').hide();
    $('#donate').show();
});
$('#hr').click(function () {
    $('#usermessage').hide();
    $('#donate').hide();
    $('#foundation').hide();
    $('#record').show();
});
$('#hf').click(function () {
    $('#usermessage').hide();
    $('#donate').hide();
    $('#record').hide();
    $('#foundation').show();
});