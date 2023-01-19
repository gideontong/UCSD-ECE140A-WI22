function toggleView(id, show) {
    var x = document.getElementById(id);
    if (show) {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function clicked(route) {
    fetch(route)
        .then(response => response.json())
        .then(function (response) {
            for (var key in response) {
                console.log(key);
                document.getElementById(key).textContent
                    = response[key];
            }
        });
    fetch('/run');
}

function select() {
    const fruit = document.getElementById('fruit').value;
    const selection = document.getElementById('selection');

    console.log(fruit);
    if (fruit == 1) {
        selection.textContent = "ITEM: Apple";
        clicked("/apple");
    } else if (fruit == 2) {
        selection.textContent = "ITEM: Orange";
        clicked("/orange");
    } else {
        selection.textContent = "ITEM: Banana";
        clicked("/banana");
    }
}