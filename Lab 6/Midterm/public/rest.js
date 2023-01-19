function toggleView(id, show) {
    var x = document.getElementById(id);
    if (show) {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function clicked() {
    fetch(`/value`)
        .then(response => response.json())
        .then(function (response) {
            for (var key in response) {
                console.log(key);
                document.getElementById(key).textContent
                    = key.toUpperCase() + ": " + response[key];
            }
        });
}

function select() {
    const sensor = document.getElementById('sensor').value;
    const type = document.getElementById('sensor_type');

    console.log(sensor);
    if (sensor == 1) {
        type.textContent = "SENSOR TYPE: Ultrasonic (HC-SR04)";
        toggleView('distance', true);
        toggleView('x', false);
        toggleView('y', false);
        toggleView('z', false);
    } else {
        type.textContent = "SENSOR TYPE: Accelrometer (MPU6050)"
        toggleView('distance', false);
        toggleView('x', true);
        toggleView('y', true);
        toggleView('z', true);
    }


    clicked();
}