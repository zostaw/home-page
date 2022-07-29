    $(document).ready(function() {
        $('#fetch').click(function(event) {
            $.ajax({
                  type: "POST",
                  url: "/process_test",
                  data: JSON.stringify("asdfasdf"),
                  contentType: "application/json",
                  dataType: 'json',
                  success: function(result) {
                    output = response;
                    alert(output);
                    console.log("Result:");
                    console.log(result);
                  } 
                });
            $('#display').html('<p> it ran for god sake </p>');
            $.getJSON('/get_records', function(data) {
                $('#display').innerHTML('<p> Name: </p>');
                $('#display').html('<p> Name: </p>');
            });
        });
    });
