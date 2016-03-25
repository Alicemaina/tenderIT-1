$(function() {	
    $( "#id_startDate" ).datepicker({
    	showAnim: 'slideDown',
    	numberOfMonths:1,
    	// dateFormat: 'dd-mm-yy',
    	minDate: 0,
    	onclose: function( selectedDate ){
    		$("#id_endDate").datepicker("option", "minDate", selectedDate);
    	}

    });
  
	
    $( "#id_endDate" ).datepicker({
    	showAnim: 'slideDown',
    	numberOfMonths:1,
    	// dateFormat: 'dd-mm-yy',
    	onclose: function( selectedDate ){
    		$("#id_startDate").datepicker("option", "maxDate", selectedDate);
    	}
    });
  });


$(document).ready(function() {
	$(".project-desc-text").dotdotdot();
});

//for company-profile tabs
$(document).ready(function(){
    $("#myTab a").click(function(e){
    	e.preventDefault();
    	$(this).tab('show');
    });
});

//update company description
$(function(){
    $('#update').click(function () {
        var mysave = $('#desc-content').html();
        $('#hiddeninput').val(mysave);
    });
});

//when decription has focus
function isFocused() {
  if (document.activeElement.id == "desc-content") {
         $('#update').css({
           'visibility' :'visible'
        });
    }
}

/*Ajx editing with Jeditable*/
function register_editables()
    {
    $(".right_click_edit").editable("/ajax/save/",
    {
    cssclass: "editable",
    width:($("span").width() + 200) + "px", // THIS DOES THE TRICK
    height:($("span#edit").height() + 25) + "px", //THIS DOES THE TRICK
    style: 'display: inline; margin-left: 10px;',
    cancel: '<button class="btn btn-default" type="cancel" >Cancel</button>',
    submit: '<button class="btn btn-primary" type="submit" >Ok</button>',
    tooltip: "Right click to edit.",
    event: "contextmenu",
    /*passing csrf_token*/
    submitdata : { csrfmiddlewaretoken : CSRF},
    });

    $(".right_click_edit_desc").editable("/ajax/save/",
    {
    type: 'textarea',
    placeholder: 'Empty description, right click to edit.',
    width:($("span").width() + 500) + "px",
    height:($("span").height() + 120) + "px",
    cssclass: 'edit_area',
    cancel: '<button class="btn btn-default" type="cancel" >Cancel</button>',
    submit: '<button class="btn btn-primary" type="submit" >Ok</button>',
    tooltip: "Right click to edit.",
    event: "contextmenu",
    /*passing csrf_token*/
    submitdata : { csrfmiddlewaretoken : CSRF},

    })
    }

$(function(){
    register_editables();
});