'use strict';

angular.module('MirrorStore.index', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: 'index/index.html',
            controller: 'indexCtrl'
        });
    }])

    .controller('indexCtrl', [function() {

    }])

    .directive('rsSlider', [function () {
        return {
            'link' : function (scope, elem, attrs) {

                $(elem).responsiveSlides({
                    auto: true,
                    pager: true,
                    nav: true,
                    speed: 1000,
                    namespace: "centered-btns"
                });

            }
        };
    }]);


