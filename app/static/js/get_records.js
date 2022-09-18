    $(document).ready(function() {
        $('#fetch').click(function(event) {
                let python_get_records = '/get_records';
                $.get(python_get_records, function(data) {
                   // Get JSON data from Python script
                   if (data){
                      console.log("Data returned:", data);
                   };
                    //var parsed_datajobDataJSON = JSON.parse(data);
                    var ddata = "<p> it ran lol "+data+".";
                    var pdata = "<p>question: " + data["question"] + " </p><p> answer: "+data["answer"] + "</p>";
                    console.log(ddata + "and" + pdata);
                    $('#display').html(pdata);
                });
        });
    });
