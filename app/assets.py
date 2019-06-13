from flask_assets import Environment, Bundle

assets_env = Environment()

common_css = Bundle(
    'vendor/nprogress/nprogress.css',
    'vendor/toastr/toastr.min.css',
    'vendor/font-awesome/css/font-awesome.min.css',
    'css/app.css',
    'css/comment/*',
    'css/layout/*',
    filters='cssmin',
    output='public/css/common.css',
)

common_js = Bundle(
    'vendor/nprogress/nprogress.js',
    'vendor/toastr/toastr.min.js',
    'js/app.js',
    filters='jsmin',
    output='public/js/common.js',
)

bundles = {
    'common_css': common_css,
    'common_js': common_js,
}
