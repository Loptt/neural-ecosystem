var socket = io();
var organisms = [];
var stage;
const WIDTH = 500;
const HEIGHT = 300;

socket.on('message', (msg) => {
    organisms = JSON.parse(msg).organisms;
})

setInterval(() => {
    socket.emit('message', 'hola!');
}, 500);

function init() {
    stage = new createjs.Stage("canvas");
    var background = new createjs.Shape();
    background.name = "background";
    background.graphics.beginFill("#1df56c").drawRect(0, 0, WIDTH, HEIGHT);
    stage.addChild(background);
    createjs.Ticker.on("tick", tick);
    createjs.Ticker.setFPS(30);
}

function tick(event) {
    var background = stage.getChildByName("background");
    stage.removeAllChildren();
    stage.addChild(background);
    for (const org of organisms) {
        console.log("Adding ", org);
        let circle = new createjs.Shape();
        circle.graphics.beginFill("DeepSkyBlue").drawCircle(org.x, org.y, org.size);
        stage.addChild(circle);
    }

    stage.update(event);
}
init();