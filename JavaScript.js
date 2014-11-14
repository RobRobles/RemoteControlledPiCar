var move_left = true;
var width = (window.innerWidth > 0) ? window.innerWidth : screen.width;

//This happens if they are a new agent trying to get access to the car
function new_agent_function() {
    $("#new_user").show();
    $("#web_cam_header").html("New Agent Form");
}

//This happens if they are a valid agent signing in
function sign_in_function() {
    $("#valid_agent").show();
    $("#sign_out_panel").show();
    $("#sign_in_panel").hide();
    $("#load_screen").hide();
    $("#pending_control").hide();
    $("#new_user").hide();
    $("#web_cam_header").html("Live Webcam");
}

//This happens when an agent signs out
function sign_out_function() {
    $("#sign_out_panel").hide();
    $("#valid_agent").hide();
    $("#pending_control").hide();
    $("#sign_in_panel").show();
    $("#load_screen").show();

}

//This moves the image at the top after two cycles of looking around
setInterval(function () {
    //if (width > 850) {
    $("#main_pic").fadeOut("slow", function () {
        x = document.getElementById("main_pic");
        p = document.getElementById("main_head");
        if (move_left == true) {
            x.style.cssFloat = "right";
            p.style.marginLeft = "40%";
            move_left = false;
            $("#main_pic").fadeIn("slow", function () {
            });
        }
        else {
            x.style.cssFloat = "left";
            p.style.marginLeft = "30%";
            move_left = true;
            $("#main_pic").fadeIn("slow", function () {
            });
        }
    });
    /*}
    else {
        document.getElementById("main_head").style.fontSize = "3.8em"
        document.getElementById("main_head").style.marginLeft = "8%";
        document.getElementById("main_head").style.position = "fixed";
        document.getElementById("main_head").style.display = "inline-block";
        document.getElementById("main_pic").style.height = "9.0em";
        document.getElementById("main_pic").style.display = "inline-block";
    }*/
}, 12500);

//This will happen after a new agent is saved to the database.
function hide_new_user_Function() {
    $("#new_user").hide();
    $("#web_cam_header").html("Live Webcam");
}

//functions to send the proper messages 

function forward(){
	//var socket = new WebSocket("ws://www.websocket.org/echo.html");
	/socket.onmessage = function(e){
	//	window.alert("message: + e.data); 
	    socket.send('forward'); 
	//window.alert("forward"); 
}

function reverse(){
	socket.send('reverse'); 
	//window.alert("reverse");
}

function upLeft(){
	socket.send('upLeft'); 
	//window.alert("upLeft");
}

function upRight(){
	socket.send('upRight'); 
	//window.alert("upRight");
}

function downLeft(){
	socket.send('downLeft'); 
	//window.alert("downLeft");
}

function downRight(){
	socket.send('downRight'); 
	//window.alert("downRight");
} 