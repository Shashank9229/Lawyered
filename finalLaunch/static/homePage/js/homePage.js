$(function(){
	var $postButton=$("#button2");
	var $inputPlace=$("#id_email_id");
	function save_email(email_val){
		
			console.log(""+$inputPlace.val());
            
            inputStr=email_val;
            console.log(email_val);
            if (inputStr.length ==0)
            {
                $(".warning").html("*Please Enter Email before Submission");
                return 0;

            }
            if (inputStr.length <6 || inputStr.indexOf('<script>')>=0 || inputStr.indexOf('@')<0 || inputStr.indexOf('.')<0)
            {
                
                $(".warning").html("*Please enter a valid Email");
                console.log("empty error");
                return 0;
            } 
            else
            {
                $("#overlay").show();
                $("#overlay div").show();
            }

			$.ajax({
				url:"register/",
				type:"POST",
				data:{
                    csrfmiddlewaretoken : csrftoken,

					posted_email : $inputPlace.val() 
				},
				success:function(json){
					if(json.result==='success'){
                        $(".warning").html("");
					}
					if(json.result==='duplicate'){
						//$(".warning").html("**This Email is already registered");
                        $(".overlay-p").html("We have already contacted you please check your email");
                        $inputPlace.val('');							
					}
                    if(json.result==='invalid'){
                        $(".warning").html("**Please enter a valid Email");
                    }
					if(json.result==='empty'){
						$(".warning").html("**Please Enter Email before Submission");	

					}
					$inputPlace.val('');
					console.log(json);
				},
				error:function(xhr,errmsg,err){
					$inputPlace.val('');
					alert("error");
							}
			});

	}
	$postButton.click(function(e){
		e.preventDefault();

		//console.log($inputPlace.val()+"ssss");
        var csrftoken = getCookie('csrftoken');
        var email_val = $inputPlace.val();
		console.log("phew working!");
		save_email(email_val);
	});


	
/*...............................................................................................................*/

    
      // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    

	
});