'use strict';

angular.module('MirrorStore.card', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/:category/:product', {
            templateUrl: 'card/card.html',
            controller: 'cardCtrl'
        });
    }])

    .controller('cardCtrl', [function() {

    }]);