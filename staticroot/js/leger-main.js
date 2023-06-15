// **** Preloader
$(window).on('load', function () { // makes sure the whole site is loaded
  $('#status').fadeOut(); // will first fade out the loading animation
  $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
  $('body').delay(350).css({ 'overflow': 'visible' });
})

// **** matchHeight
// $('.matchHeight').matchHeight();

// **** Fancybox
// $('.fancybox').fancybox({
//   beforeLoad: function() {
//     var el, id = $(this.element).data('title-id');
//     if (id) {
//       el = $('#' + id);

//       if (el.length) {
//         this.title = el.html();
//       }
//     }
//   }
// });

// $('.fancybox-media')
// .attr('rel', 'media-gallery')
// .fancybox({
//   openEffect : 'none',
//   closeEffect : 'none',
//   prevEffect : 'none',
//   nextEffect : 'none',
//   arrows : false,
//   helpers : {
//     media : {},
//     buttons : {}
//   }
// });


// **** AOS : Animate On Scroll Library
// **** https://michalsnik.github.io/aos/
AOS.init();

//  **** tooltip bootstrap
// $('[data-toggle="tooltip"]').tooltip({
//   container: 'body'
// })

// ****Slick
$('.slick-carousel-1').slick({
  dots: true,
  infinite: true,
  slidesToShow: 3,
  slidesToScroll: 3
});

// **** Slick header
$('.bandeau-slider.slider-header').slick({
  dots: false,
  arrows: false,
  infinite: true,
  autoplay: true,
  autoplaySpeed: 0,
  speed: 10000,
  cssEase: 'linear',
  centerMode: true,
  variableWidth: true
});


// **** Menu vertical accordéon *base*
$(".openCat").click(function(event){
  var classNext=$(this).next("ul").attr("class")
  $(".openCat").each(function(){
    if($(this).next("ul").attr("class")==classNext){
      $(this).removeClass("active")
    }
  })
  $(".openCat").next("ul."+classNext).slideUp(400);
  if($(this).next().is(":hidden")){
    $(this).next().slideDown(400);
    $(this).toggleClass("active");
  }
  return false;
});

// **** Imprim pour page compte-client.asp
$(".imprim").click(function(){
  var id = $(this).attr("id").substr(7)
  var f = window.open("../outils/CompteClient/printfacture.asp?id="+id, "ZoneImpr", "height=700, width=1000, toolbar=1, menubar=1, scrollbars=1, resizable=1, status=0, location=0, left=10, top=10");
  return false
});


// **** Slide toogle (dans navbar E-commerce)
$('#dropdown-search').hide().click(function(event) {
  event.stopPropagation();
});
$('html,body,.btn-cart,.btn-account,.btn-close').on('click', function(event) {
  $('#dropdown-search').slideUp();
});
$( ".btn-search" ).click(function(event) {
  $( "#dropdown-search" ).slideToggle();
  event.stopPropagation();
});

$('#dropdown-cart').hide().click(function(event) {
  event.stopPropagation();
});

$('html,body,.btn-search,.btn-account,.btn-close').on('click', function(event) {
  $('#dropdown-cart').slideUp();
});
$( ".btn-cart" ).click(function(event) {
  $( "#dropdown-cart" ).slideToggle();
  event.stopPropagation();
});

$('#dropdown-account').hide().click(function(event) {
  event.stopPropagation();
});
$('html,body,.btn-search,.btn-cart,.btn-close').on('click', function(event) {
  $('#dropdown-account').slideUp();
});
$( ".btn-account" ).click(function(event) {
  $( "#dropdown-account" ).slideToggle();
  event.stopPropagation();
});

$(window).scroll(function(event) {
  $( "#dropdown-account, #dropdown-cart, #dropdown-search" ).slideUp();
  event.stopPropagation();
  return false;
});


// **** Slider propositions */
$('.slider-proposition').slick({
  dots: true,
  infinite: false,
  speed: 300,
  slidesToShow: 3,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 800,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});