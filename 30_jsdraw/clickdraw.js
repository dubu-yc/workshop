//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D Object
var ctx = c.getContext("2d");

//intit global state var
var mode = "rect";
var toggler = document.getElementById("buttonToggle");


//var toggleMode = function(e) {
var toggleMode = (e) => {
    if (mode == "rect") {
        mode = "circle";
        toggler.innerHTML = "Circle"
    } else {
        mode = "rect";
        toggler.innerHTML = "Rect"
    }
}

toggler.addEventListener("click", toggleMode);

var draw = (e) => {
    if (mode == "rect") {
       drawRect(e);
    } else {
        drawCircle(e);
    }
}

var drawRect = (e) => {
    let mouseX = e.offsetX;
    let mouseY = e.offsetY;

    ctx.rect(mouseX, mouseY, 100, 150)
    ctx.fillStyle = "green"
    ctx.fill()
}

var drawCircle = (e) => {
    let mouseX = e.offsetX;
    let mouseY = e.offsetY;
    
    ctx.beginPath()
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI)
    ctx.fillStyle = "blue"
    ctx.fill()
    ctx.stroke()
}

var clearButton = document.getElementById("buttonClear")

var wipeCanvas = function() {
    ctx.clearRect(0, 0, c.clientWidth, c.height)
}

clearButton.addEventListener("click", wipeCanvas);

c.addEventListener("click", draw)