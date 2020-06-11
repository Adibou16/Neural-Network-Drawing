// Variable Declaration
const canvas = document.querySelector("canvas");
const clearButton = document.querySelector("#clear");
const ctx = canvas.getContext("2d");
const scale = 10;
const arraySize = 28;
const rows = canvas.height / scale;
const columns = canvas.width / scale;

var drawing;
var x;
var y;

var array = new Array(arraySize);



// Setup: Clears Screen and Resets Array
function setup() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (var i = 0; i < arraySize; i++) {
        array[i] = new Array(arraySize);
    }
}
setup()



// Draw loop
function draw() {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array[i].length; j++) {
            ctx.beginPath();
            ctx.rect(i * scale, j * scale, scale, scale);
            ctx.fillStyle = array[i][j] ? "white" : "gray";
            ctx.fill();
        }
    }
    requestAnimationFrame(draw);
}
requestAnimationFrame(draw);



// Drawing
function pen(event) {
    let x = Math.floor(event.clientX / scale);
    let y = Math.floor(event.clientY / scale);

    array[x][y] = 1;
}



// Mouse Listeners
let clicked = false
canvas.addEventListener("mousedown", (e) => {
    clicked = true;
    pen(e);
});

canvas.addEventListener("mouseup", () => {
    clicked = false;
});

canvas.addEventListener("mousemove", (e) => {
    if (clicked) pen(e);
});

canvas.addEventListener("mouseleave", () => {
    clicked = false;
});



// Clear Button Listener
clearButton.addEventListener("click", setup);