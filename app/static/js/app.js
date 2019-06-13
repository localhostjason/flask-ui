$(document).ready(function () {
    $("[data-toggle='popover']").popover({
        placement: 'top',
        trigger: 'hover',
        html: true
    });
    $("[data-toggle='tooltip']").tooltip();

    NProgress.start();
    NProgress.done();

    toastr.options = {
        "closeButton": true,
        "timeOut": 2000
    };

    window.setTimeout(function () {
        $(".toast-top-right.dis_pos").fadeTo(1000, 0).slideUp(1000, function () {
            $(this).alert('close');
        });
    }, 2000);
    $('.toast-close-button.dis_show').click(function () {
        $('.toast-top-right.dis_pos').css('display', 'none')
    });


    let retract = 'retract';

    function expend_aside() {
        let btn_fold_menu = $('.btn-fold-menu');
        let text = btn_fold_menu.attr('title');
        if (text === '收起') {
            btn_fold_menu.addClass(retract);
            btn_fold_menu.attr('title', '展开').text('展开');
            $('.container-fluid-base').css("left", -203);
        } else {
            btn_fold_menu.removeClass(retract);
            btn_fold_menu.attr('title', '收起').text('收起');
            $('.container-fluid-base').css("left", 0);
        }
    }

    function resize_width() {
        let window_width = $(window).width();
        let btn_fold_menu = $('.btn-fold-menu');
        let text = btn_fold_menu.attr('title');
        if (window_width < 1200) {
            btn_fold_menu.addClass(retract);
            btn_fold_menu.attr('title', '展开').text('展开');
            $('.container-fluid-base').css("left", -203);
        } else {
            btn_fold_menu.removeClass(retract);
            btn_fold_menu.attr('title', '收起').text('收起');
            $('.container-fluid-base').css("left", 0);
        }
    }

    resize_width();
    $(window).resize(resize_width);
    $('.btn-fold-menu').click(function () {
        expend_aside()
    });


    let toggle_menu = $('.aside-menu-v2-toggle');

    toggle_menu.each(function (index, el) {
        $(this).click(function () {
            $(this).toggleClass('open');
        })
    });

    if (sessionStorage.getItem("success")) {
        toastr.success(sessionStorage.getItem("success"));
        sessionStorage.clear();
    }
    if (sessionStorage.getItem("error")) {
        toastr.error(sessionStorage.getItem("error"));
        sessionStorage.clear();
    }
    if (sessionStorage.getItem("warning")) {
        toastr.warning(sessionStorage.getItem("warning"));
        sessionStorage.clear();
    }

    if (sessionStorage.getItem("info")) {
        toastr.info(sessionStorage.getItem("info"));
        sessionStorage.clear();
    }

});

;(function ($, window, undefined) {
    let $allDropdowns = $();
    $.fn.dropdownHover = function (options) {

        $allDropdowns = $allDropdowns.add(this.parent());

        return this.each(function () {
            var $this = $(this).parent(),
                defaults = {
                    delay: 200,
                    instantlyCloseOthers: true
                },
                data = {
                    delay: $(this).data('delay'),
                    instantlyCloseOthers: $(this).data('close-others')
                },
                options = $.extend(true, {}, defaults, options, data),
                timeout;

            $this.hover(function () {
                if (options.instantlyCloseOthers === true)
                    $allDropdowns.removeClass('open');

                window.clearTimeout(timeout);
                $(this).addClass('open');
            }, function () {
                timeout = window.setTimeout(function () {
                    $this.removeClass('open');
                }, options.delay);
            });
        });
    };

    $('[data-hover="dropdown"]').dropdownHover();
})(jQuery, this);


$(document).ready(function () {
    $.update_info_reload = function (msg, url, params) {
        Modal.confirm({
            msg: msg
        }).on(function (e) {
            if (e) {
                $.post(url, params, function (data) {
                    if (data.success) {
                        sessionStorage.setItem("success", data.message);
                        window.location.reload();
                    } else {
                        toastr.error(data.message);
                    }
                })
            }
        })
    };


    $.del_info_reload = function (msg, url, params, load_href) {
        Modal.confirm({
            msg: msg
        }).on(function (e) {
            if (e) {
                $.post(url, params, function (data) {
                    if (data.success) {
                        sessionStorage.setItem("success", data.message);
                        location.href = load_href;
                    } else {
                        toastr.error(data.message);
                    }
                })
            }
        })
    };


});


jQuery.cachedScript = function (url, options) {

    options = $.extend(options || {}, {
        dataType: "script",
        cache: true,
        url: url
    });

    return jQuery.ajax(options);
};