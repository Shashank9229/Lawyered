$(function(){
    //Headline Changes.............................................................
	var $textArea=$("#change-stuff");
    var textNames=['buisnesses','artists','entrepreneurs','startups','freelancers'];
    var count=0;
    function changeText(){
    	text=textNames[count]+'';
        $textArea.html(text);
        count=count+1;
        if(count>(textNames.length)-1){
            count=0;
        }
    }
   setInterval(changeText,2000);
 
    console.log("xx");

    //Smoooth Scroll...........................................................
    $('#will-scroll').click(function(e){
        e.preventDefault();
        $('html,body').animate({
            scrollTop:$('#connect-us').offset().top
        },800);
    });
});