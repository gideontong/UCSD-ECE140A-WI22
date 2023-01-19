function clicked() {
    const age = document.getElementById('age2').value;
    const height = document.getElementById('height2').value;

    fetch(`/value/${age}/${height}`)
        .then(response => response.json())
        .then(function (response) {
            for (var key in response) {
                console.log(key);
                document.getElementById(key).textContent
                    = key.toUpperCase() + ": " + response[key]
            }
            document.getElementById('image').src = response['name'];
        });
}
