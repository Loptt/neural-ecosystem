import {Camera} from './camera.js';

var socket = io();
var organisms = [];
var foods = [];
var stage;
var documentWidth = 1000;
var documentHeight = 1000;
var camera = new Camera(0, 0);

socket.on('message', (msg) => {
    organisms = JSON.parse(msg).organisms;
    foods = JSON.parse(msg).foods;
})

setInterval(() => {
    socket.emit('message', 'hola!');
}, 100);

function init() {
    // Configure canvas to window size.
    var canvas = document.getElementById('canvas');
    documentWidth = window.innerWidth;
    documentHeight = window.innerHeight;

    canvas.width = documentWidth;
    canvas.height = documentHeight;

    // Set up canvas with createjs
    stage = new createjs.Stage("canvas");

    var background = new createjs.Shape();
    background.name = "background";
    background.graphics.beginFill("#5ac700").drawRect(0, 0, documentWidth, documentHeight);
    /*
    background.on("pressmove", (e) => {
        camera.x = e.stageX;
        camera.y = e.stageY;
        console.log(e);
    });
    */
    stage.addChild(background);

    // Set up ticker
    createjs.Ticker.on("tick", tick);
    createjs.Ticker.setFPS(30);
}

function tick(event) {
    var background = stage.getChildByName("background");
    stage.removeAllChildren();
    stage.addChild(background);
    let transformedOrgs = camera.transform(organisms);
    console.log(transformedOrgs[0])
    let transformedFoods = camera.transform(foods);

    for (const org of transformedOrgs) {
        let circle = new createjs.Shape();
        circle.graphics.beginFill("#e2e610").drawCircle(org.x, org.y, org.size);
        stage.addChild(circle);
    }

    for (const food of transformedFoods) {
        let circle = new createjs.Shape();
        circle.graphics.beginFill("#f58a42").drawCircle(food.x, food.y, 10);
        stage.addChild(circle);
    }

    stage.update(event);
}
init();