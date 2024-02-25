$(document).ready(function() {
    var $body = $("body");

    $('#countdown').on('submit', function(event) {
        event.preventDefault();
        $body.addClass("loading");
            $.ajax({
                url: '', 
                type: 'get', 
                data: {
					number1: $('#number1').val(),
					number2: $('#number2').val(),
					number3: $('#number3').val(),
					number4: $('#number4').val(),
					number5: $('#number5').val(),
					number6: $('#number6').val(),
					target: $('#target').val(),
					shortest: $('#shortest').prop('checked'),
                },
                success: function(response) {
                    $('#result').html('<b>Result: </b>' + response.result); 
                },
                error: function(xhr, status, error) {
                    $('#result').html('<b>Error: </b>' + error); 
                },
                complete: function() {
                    $body.removeClass("loading");
                }
            });
    });
});



$(function() {
    $("input").keypress(function(event) {
        if (event.which != 8 && event.which !== 0 && (event.which < 48 || event.which > 57)) {
            $(".alert").html("Enter only digits!").show().fadeOut(2000);
            return false;
        }
    });
});

$(document).ready(function () {
$('input.dcp').bind('copy paste', function (e) {
   e.preventDefault();
});
});
//document.addEventListener('contextmenu', event => event.preventDefault());