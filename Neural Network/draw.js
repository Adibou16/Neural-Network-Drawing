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


function draw() {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array[i].length; j++) {
            ctx.beginPath();
            ctx.rect(i * scale, j * scale, scale, scale) 
            ctx.fillStyle = array[i][j] ? "white" : "gray";
            ctx.fill()
        }
    }

    requestAnimationFrame(draw);
}
requestAnimationFrame(draw);

function pen(event) {
    let x = Math.floor(event.clientX / scale)
    let y = Math.floor(event.clientY / scale)

    array[x][y] = 1
}

let clicked = false
canvas.addEventListener("mousedown", (e) => {
    clicked = true
    pen(e)
});

canvas.addEventListener("mouseup", () => {
    clicked = false
});

canvas.addEventListener("mousemove", (e) => {
    if(clicked) pen(e)
});