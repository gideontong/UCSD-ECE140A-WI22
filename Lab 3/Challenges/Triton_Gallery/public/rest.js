function click_display() {
    const display = document.getElementById('image');
    const inn = document.getElementById('in');

    display.src = `/photos/${inn.value}.jpg`;
}

function click_price() {
    const inn = document.getElementById('in');
    const priceBox = document.getElementById('price');

    fetch(`/price/${inn}`)
        .then((data) => {
            data.text().then((text) => {
                priceBox.innerText = text;
            })
        });
}