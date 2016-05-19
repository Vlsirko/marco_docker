'use strict'

angular.module('MirrorStore.basket', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/basket', {
            templateUrl: 'basket/basket.html',
            controller: 'basketCtrl'
        });
    }])

    .controller('basketCtrl', function($scope, $routeParams, Product, $cookies) {
        $scope.basket = $cookies.getObject('basket');
        $scope.empty = Object.keys($scope.basket).length === 0;

        Product.get({ids:  Object.keys($scope.basket).join(',')}, function (data) {
            $scope.products = data.results;
        });

        $scope.removeFromCard = function(id){
            delete $scope.basket[id];
            $scope.empty = Object.keys($scope.basket).length === 0;
            $cookies.putObject('basket', $scope.basket)
        }

        $scope.changeQuantity = function(){
            $cookies.putObject('basket', $scope.basket)
        }

    });
