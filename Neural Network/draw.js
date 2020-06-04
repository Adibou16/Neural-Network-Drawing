const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");
const scale = 10;
const rows = canvas.height / scale;
const columns = canvas.width / scale;

var drawing;
var x;
var y;

var array = new Array(30);

for (var i = 0; i < 30; i++) {
    array[i] = new Array(30);
}

console.log(array);

function newDrawing(x, y) {
    drawing = new Drawing(x - 1, y - 1);
    drawing.draw();
}

function Drawing(x, y) {
    this.draw = function() {
        ctx.fillStyle = "white";
        ctx.fillRect(x * 10, y * 10, scale, scale);
    }
}

canvas.addEventListener("click", newDrawing(15, 30));