$(document).ready(function() {
    let all_boxes_list;
    var answer = document.getElementById('space-rep-answer').value;
    console.log(answer);
    // prepare for API
    const dict_values = {answer}; //Pass the javascript variables to a dictionary.
    const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
    var pdata = "<p>" + "Questions will appear here. After writing down your answers, click Submit to verify.\n" +
    "The answers must fit exactly the wording, it helps to memorize the concept, because one needs to remember the details.\n" +
    "Click Start when you're ready..." + "</p>"
    $('#ds_output').html(pdata);


    function presentBox(boxes_list, box_id){
        // returns HTML formatted string, presents all records in a box, separated by paragraphs
        var box = boxes_list[box_id];
        var record_id = 0;
        var pdata = "<p>";
        while(box[record_id]){
            // collect and format HTML string for all records in a box: name, question, answer
            if(box[record_id][1]){
                pdata = pdata + "<b>" + box[record_id][1] + "</b></br>";
            }

            pdata = pdata + "<b>Question: </b>" + box[record_id][2] + "</br>" +
            "<b>Answer: </b>" + box[record_id][3] + "</p>";

            record_id++;
        }
        console.log(pdata);
        return pdata;
    }

    $('#fetch').click(function(event) {
        // read from textbox
        var answer = document.getElementById('space-rep-answer').value;
        console.log(answer);

        if(all_boxes_list == undefined){
            const s = JSON.stringify(''); // Stringify converts a JavaScript object or value to a JSON string

            // post to python API
            $.ajax({
                url: "/sr_get_all_boxes",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify(s),
                success: function( data, status, xhttp) {
                    // data is value returned from API
                    all_boxes_list = data;
                    // Present the first box immediatelly:
                    $('#ds_output').html(presentBox(all_boxes_list, 0));
                    $('#fetch').html("Submit");
                }
            });
        }
        else{
            // TODO: define logic:
            // - what should happen after first box is presented
            // - define how to transition between boxes
            // - handle answers
            $('#ds_output').html(presentBox(all_boxes_list, 0));
        }


    });
});
