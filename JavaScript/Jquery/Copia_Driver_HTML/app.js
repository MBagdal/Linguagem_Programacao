var name_folder;
$('.click').on({
	mousedown: function(event){
  	switch(event.which){
  		case 1:
      	
      	$(".click").css("background-color", "#fff");
        $("p").css("color", "#000");
      	$(this).css('background-color','#39f');  
        $(this).find("p").css("color", "#fff");
        name_folder = $(this).find("p").text();
        
      break;
     case 3:
     		$(".click").css("background-color", "#fff");
        $("p").css("color", "#000");
      	$(this).css('background-color','#39f');  
        $(this).find("p").css("color", "#fff");
        $(".menu").find("p").text("Menu " + $(this).find("p").html()).css({'color':'#000', 'padding': '10px'});
        name_folder = $(this).find("p").text();
        break;   
     default:
      	$("#result").html("Que mouse e esse fera?");
  	}	
	},
  contextmenu: function(event){
  	event.preventDefault();
  	Menu();
  }
});
	
	
var Menu = function(){
					var menu = $(".menu"); 

		       //hide menu if already shown
		       menu.hide(); 
		       
		       //get x and y values of the click event
		       var pageX = event.pageX;
		       var pageY = event.pageY;

		       //position menu div near mouse cliked area
		       menu.css({top: pageY , left: pageX});

		       var mwidth = menu.width();
		       var mheight = menu.height();
		       var screenWidth = $(window).width();
		       var screenHeight = $(window).height();

		       //if window is scrolled
		       var scrTop = $(window).scrollTop();

		       //if the menu is close to right edge of the window
		       if(pageX+mwidth > screenWidth){
		       	menu.css({left:pageX-mwidth});
		       }

		       //if the menu is close to bottom edge of the window
		       if(pageY+mheight > screenHeight+scrTop){
		       	menu.css({top:pageY-mheight});
		       }
		       //finally show the menu
		       menu.show();
}

$(".menu li").click(function(){
    var operacao = $(this).html();
    alert("Voce Irar " + operacao + " a pasta " + name_folder);
  });
  
$("html").on("click", function(){
			$(".menu").hide();
});