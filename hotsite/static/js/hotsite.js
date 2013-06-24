'use strict';


// content slider
+function ($) {

	function switch_page(name) {
	    var links = $('#main_nav a'),
		    pages = $('#content > section'),
		    link = links.filter('[href$="#'+name+'"]'),
		    page = pages.filter(function () {
		    	return !!$('a[name="'+name+'"]', this).length
		    });

		// switch menu item state
		links.removeClass('selected');
		link.addClass('selected');

		// switch content sections visibility
		pages.hide();
		page.show();
	}

	// #main_nav links click
	$('#main_nav').on('click', 'a', function (e) {
		var name = $(this).attr('href').split('#')[1];
		switch_page(name);
	});

	// initial load
	var initial_page = (location.hash || location.href).split('#')[1] ||
		$('#content > section > a[name]:first').attr('name');
	switch_page(initial_page);

}(jQuery);
