var app = angular.module('marco', ['ngRoute', 'ngAnimate'])

    .config(['$interpolateProvider', function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    }])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: '/s/frontend/templates/index.html',
        }).when('/catalog/:category_alias', {
            templateUrl: '/s/frontend/templates/catalog.html',
            controller: 'ProductsListingController'
        }).when('/phones/:phoneId', {
            templateUrl: '/s/partials/phone-detail.html',
            controller: 'PhoneDetailCtrl'
        }).otherwise({
            redirectTo: '/#/'
        });
    }]);