$(document).ready(function() {
    $("#searchbox").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $('div[data-role="list-menus"]').filter(function() {
            $(this).toggle($(this).find('a').text().toLowerCase().indexOf(value) > -1)
        });
    });
});

$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#leftSidebar').toggleClass('toggled');
        $('#rightScreen').toggleClass('toggled'); 
        $('#buttonTest').attr("aria-expanded","false");
        $('.button1').addClass('collapsed');   
        $('.buttonTest2').removeClass('show');
    });
});

$(document).ready(function () {
    var typed = new Typed('#typed', {
    stringsElement: '#typed-strings',
    typeSpeed: 40, //ini waktu ngetiknya
    showCursor: false
    });

    var typed = new Typed('#typed-2', {
    stringsElement: '#typed-strings-2',
    typeSpeed: 40,
    startDelay: 2000, //ini delay sebelum mulai, dalam ms semua
    showCursor: false
    });
});
