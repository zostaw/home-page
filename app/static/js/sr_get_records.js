$(document).ready(function() {
    var answer = document.getElementById('space-rep-answer').value;
    console.log(answer);
    // prepare for API
    const dict_values = {answer}; //Pass the javascript variables to a dictionary.
    const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
    // post to python API
    $.ajax({
        url: "/sr_get_all_boxes",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(s),
        success: function( data, status, xhttp) {
            // data is value returned from API
            console.log(data);
            // print output on page
            //var pdata = "<p>question: " + data["question"] + " </p><p> answer: "+data["answer"] + "</p>";
            var pdata = "<p>" + data + "</p>"
            $('#ds_output').html(pdata);
        }
    });

    $('#fetch').click(function(event) {
        // read from textbox
        var answer = document.getElementById('space-rep-answer').value;
        console.log(answer);
        // prepare for API
        const dict_values = {answer}; //Pass the javascript variables to a dictionary.
        const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
        // post to python API
        $.ajax({
            url: "/sr_get_all_boxes",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(s),
            success: function( data, status, xhttp) {
                // data is value returned from API
                console.log(data);
                // print output on page
                //var pdata = "<p>question: " + data["question"] + " </p><p> answer: "+data["answer"] + "</p>";
                var pdata = "<p>" + data + "</p>"
                $('#ds_output').html(pdata);
            }
        });
    });
});
