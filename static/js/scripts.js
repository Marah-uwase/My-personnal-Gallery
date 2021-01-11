$("[data-fancybox]").fancybox({
    "onComplete": function() {
      console.log('open');
      $('.fancybox-placeholder').css('padding', '40px');
    },
    "beforeClose": function() {
      console.log('close');
      $('.fancybox-placeholder').css('padding', '');
      // fancybox is closed, run myOtherFunct()
    }
  })
