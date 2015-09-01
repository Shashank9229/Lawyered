/*
$(document).ready(function(){
	
	var numberOfSlides=3;//number of slides
	var widthRequired=3;
	$('.slide').css('width', $(window).innerWidth()+'px');
	$('.sliders').css('width',($(window).innerWidth()*widthRequired)+'px');
	$('#recent-post-banner').css('width',($(window).innerWidth())+'px');
	console.log($(window).innerWidth());
	console.log($(window).innerWidth()*widthRequired);
	$(window).resize(function(){
		$('.slide').css('width', $(window).innerWidth()+'px');
		$('.sliders').css('width',($(window).innerWidth()*widthRequired)+'px');
		$('#recent-post-banner').css('width',($(window).innerWidth())+'px');

	var animationSpeed=1000;
	var pause=5000;
	var currentSlide=1;
	var width=$(window).innerWidth();
	var $slider=$('#recent-post-banner');
	var $slideContainer=$('.slides',$slider);
	var $slides=$('.slide',$slider);
	var $leftSlideButt=$('.slider-left',$slides);
	var $rightSlideButt=$('.slider-right',$slides);
	var interval;
		pauseSlider();
		startSlider();
		
	});


	//Slider Stuff....................

	//Settings for slider
	var animationSpeed=1000;
	var pause=5000;
	var currentSlide=1;
	var width=$(window).innerWidth();
	var interval;
	//console.log(width);

	//Dom events
	var $slider=$('#recent-post-banner');
	var $slideContainer=$('.slides',$slider);
	var $slides=$('.slide',$slider);
	var $leftSlideButt=$('.slider-left',$slides);
	var $rightSlideButt=$('.slider-right',$slides);
	//$slideContainer.first().css('margin-left',''+width);
	
	function startSlider(){
		interval=setInterval(function(){
			$slideContainer.animate({'margin-left':'-='+$(window).innerWidth()},
				animationSpeed,function(){
					if(++currentSlide ===$slides.length){
						currentSlide=1;
						$slideContainer.css('margin-left','0');
					}
					
				});
		},pause);
	}
	function pauseSlider(){
		clearInterval(interval);	
	}
	function slideLeft(e){
		e.preventDefault();
		if(currentSlide===1){
			$slideContainer.css({'margin-left':''-$(window).innerWidth()*3});
			console.log("sss");
			$slideContainer.animate({'margin-left':'+='+$(window).innerWidth()},
				animationSpeed,function() {
					$slideContainer.css('margin-left',''-$(window).innerWidth()*2);
				});
			currentSlide=$slides.length;
		}
		else{
			$slideContainer.animate({'margin-left':'+='+$(window).innerWidth()},animationSpeed);
			currentSlide=currentSlide-1;

		}
	}
	function slideRight(e){
		e.preventDefault();
		if(currentSlide===$slides.length){
			
			console.log($(window).innerWidth());
			$slideContainer.css('margin-left',''+$(window).innerWidth());
			currentSlide=1;
			$slideContainer.animate({'margin-left':'-='+$(window).innerWidth()},animationSpeed,function(){
				$slideContainer.css('margin-left','0');
			});
		}
		else{
			$slideContainer.animate({'margin-left':'-='+$(window).innerWidth()},animationSpeed);
			currentSlide=currentSlide+1;
		}
	}
	$slideContainer.on('mouseenter',pauseSlider).on('mouseleave',startSlider);
	$leftSlideButt.on('click',slideLeft);
	$rightSlideButt.on('click',slideRight);

	startSlider();
	*/

	$(function() {
    $(".rslides").responsiveSlides();
  });