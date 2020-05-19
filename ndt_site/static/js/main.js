(function($) { // Begin jQuery
    $(function() { // DOM ready


        //hides drop down when link is clicked
        $("nav li").click(function () {
          $('.nav-list').hide();
          $("#nav-toggle").toggleClass('active').show();

        });

        // Toggle open and close nav styles on click
        $('#nav-toggle').click(function(e) {
          e.preventDefault();
          $('nav ul').slideToggle();
        });

        // Hamburger to X toggle
        $('#nav-toggle').on('click', function() {
          this.classList.toggle('active');
        });

        var swiper = new Swiper('.swiper-container', {
          slidesPerView: 1,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
          }
        });
      
        var typed = new Typed('.type', {
          strings: ["Mastercraft", "Moomba", "Sea Ray", "Yamaha", "Tige", "Bayliner", "Crownline", "Sea Doo", "Nautique", "Supra", "Malibu", "Four Winns", "Startcraft", "Centurion", "Stingray", "Cobalt", "Bryant"],
          typeSpeed: 100, 
          loop: true
        });

        //Bimini page js for image changer
        $('.color-choose input').on('click', function() {
          var biminiColor = $(this).attr('data-iamge');
          console.log(biminiColor);
          $('.active').removeClass('.active');
          $('.left-column img[data-image = ' + biminiColor + ']').addClass('active');
          $(this).addClass('.active');
        });

    }); // end DOM ready
  })(jQuery); // end jQuery
