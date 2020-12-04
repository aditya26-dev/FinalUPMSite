$(document).ready(function() {
    $("#searchbox").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $('div[data-role="card-menus"]').filter(function() {
            $(this).toggle($(this).find('h5').text().toLowerCase().indexOf(value) > -1)
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