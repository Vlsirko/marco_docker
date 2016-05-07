'use strict';

angular.module('MirrorStore.card', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/:category/:product', {
            templateUrl: 'card/card.html',
            controller: 'cardCtrl'
        });
    }])

    .controller('cardCtrl', function($scope, $http, $routeParams) {
        var product_alias = $routeParams.product;
        $http.get('/api/products/'+product_alias).success(function(data) {
            $scope.product = data;
            $scope.description = data.description;
        });
    });