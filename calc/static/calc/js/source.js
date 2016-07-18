        var form = document.getElementById("num");
        var result = document.getElementById("result");
        var equ = document.getElementById("equally");
        var cle = document.getElementById("clean");
        var clElm = document.getElementById("cleanElm");

        clElm.addEventListener("click",fcleanElm);
        cle.addEventListener("click",fclean);
        equ.addEventListener("click",senData);

        function fcleanElm(){
            result.value = result.value.slice(0,-1)
        }
        function fclean (){
            result.value = '';
        }


 form.onclick = function(e){
            var target = e.target;
            if (target.tagName == 'INPUT'){
            result.value += target.value;
            }
        };

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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function senData(){
    console.log("Result value " + result.value)
    console.log("send data is working!")
    $.ajax({
        url : "/calc/", // the endpoint
        type : "POST", // http method
        data : { value_exp :  result.value },

        // handle a successful response
        success : function(json) {
            result.value = json.val_exp
            console.log(json);
            console.log("success");
        },

        // handle a non-successful response
        error : function(xhr,errmsg) {
            $('#results').html("<div  data-alert>Oops! We have encountered an error: "+errmsg+"</div>");
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
}