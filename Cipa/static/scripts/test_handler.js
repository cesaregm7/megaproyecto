
function checkComplete()
{
	if (jQuery(".btn-group-justified").length == jQuery(".btn-success").length ||
		jQuery(".btn-group-vertical").length == jQuery(".btn-success").length)
	{
		var questions = [];
		var answers = [];
		
		var form = jQuery("#test_form");
	
		jQuery("tr.tr-question").each(function ()
		{
			row = jQuery(this);
			var q = row.find("td.id-test-question").html();
			var a = row.find("a.btn-success").html();
			questions.push(q);
			answers.push(a);

			form.prepend("<input type=\"hidden\" name=\""+q+"\" value=\""+a+"\">\n");
		});

		jQuery(".invisible").removeClass("invisible");
	}
}

jQuery(".btn").on('click touch',function()
	{
		var clicked_btn = jQuery(event.target);
		var classList = clicked_btn.attr('class').split(/\s+/);
		
		if (jQuery.inArray("btn-submit", classList) == -1)
		{
			jQuery("."+classList[2]).removeClass("btn-success");
			clicked_btn.addClass("btn-success");
			checkComplete();
			console.log("yeap");
		}
		else
		{
			var questions = [];
			var answers = [];
			var token = jQuery('input[name=csrfmiddlewaretoken]').attr("value");

			jQuery("tr.tr-question").each(function ()
			{
				row = jQuery(this);
				questions.push(row.find("td.id-test-question").html());
				answers.push(row.find("a.btn-success").html());
			});
		}
	});

jQuery(window).resize(function() {
  if ($(window).width() < 480) {
    jQuery('.btn-group-responsive').removeClass('btn-group-justified');
    jQuery('.btn-group-responsive').addClass('btn-group-vertical');
  } else {
    jQuery('.btn-group-responsive').addClass('btn-group-justified');
    jQuery('.btn-group-responsive').removeClass('btn-group-vertical');
  }
});

