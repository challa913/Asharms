/**
 * Created by nischal on 9/11/14.
 */

$(document).ready(function() {
    $("#home").click(function () {
        alert('home');
    });

    $("#needs").click(function () {
        alert('Track');
    });

    $("#donations").click(function () {
        alert('sign-in');
    });
    $("#ashrams").click(function () {
        alert('sign-in');
    });
    $("#about").click(function () {
        alert('sign-in');
    });
    $("#contact").click(function () {
        alert('sign-in');
    });
     $("#header-donate-button , #track-donation, #sign-in").hover(function(){
    $("#header-div").css("cursor","pointer");
    },function(){
    $("#header-div").css("cursor","default");
  });
});
