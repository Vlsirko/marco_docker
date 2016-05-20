'use strict';

// Declare app level module which depends on views, and components
angular.module('MirrorStore', [
    'ngRoute',
    'ngResource',
    'ngAnimate',
    'ngSanitize',
    'ngCookies',
    'services',
    'MirrorStore.index',
    'MirrorStore.catalog',
    'MirrorStore.card',
    'MirrorStore.basket'
]).config(['$routeProvider', function ($routeProvider) {
    $routeProvider.otherwise({redirectTo: '/'});
}]).config(function($httpProvider) {
    $httpProvider.interceptors.push(function($q) {
        var realEncodeURIComponent = window.encodeURIComponent;
        return {
            'request': function(config) {
                window.encodeURIComponent = function(input) {
                    return realEncodeURIComponent(input).split("%2B").join("+");
                };
                return config || $q.when(config);
            },
            'response': function(config) {
                window.encodeURIComponent = realEncodeURIComponent;
                return config || $q.when(config);
            }
        };
    });

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});


