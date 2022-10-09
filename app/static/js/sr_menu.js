
function menuFunction() {
        //value = document.querySelector("#menu");
        const sb = document.querySelector('#menu_list')
        option = sb.options[sb.value].text;
        console.log(option);
        //$('#option_name').html(option);
        // div with same id name as menu option must be defined
        document.getElementById(option).style.display = "block";
};

