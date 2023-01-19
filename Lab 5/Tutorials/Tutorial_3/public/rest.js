function select_staff() {
    let staff_id = document.getElementById('staff').value;
    if (staff_id.trim() === "") {
        console.log("No ID provided");
        document.getElementById("error").textContent = "You have not provided an ID";
    }
    else {
        let theURL = '/staff/' + staff_id;
        console.log("Starting executing single id");
        document.getElementById("error").textContent = "";
        fetch(theURL)
            .then(response => response.json())
            .then(function (response) {
                for (var key in response) {
                    document.getElementById(key).textContent
                        = key.toUpperCase() + ": " + response[key]
                }
            });
    }
}
