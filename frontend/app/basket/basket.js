'use strict'

angular.module('MirrorStore.basket', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/basket', {
            templateUrl: 'basket/basket.html',
            controller: 'basketCtrl'
        });
    }])

    .controller('basketCtrl', function($rootScope, $scope, $routeParams, Product, $cookies, Order, $uibModal) {
        $scope.basket = $cookies.getObject('basket') ? $cookies.getObject('basket') : {};
        $scope.empty = Object.keys($scope.basket).length === 0;
        $scope.amount = 0;

        $rootScope.title = 'MirrorStore: Корзина';
        
        if(!$scope.empty) {

           Product.get({ids: Object.keys($scope.basket).join(',')}, function (data) {

               $scope.products = data.results;

               $scope.$watch(function () {
                    var amount = 0;
                    for (var product in data.results) {
                        var quantity = $scope.basket[data.results[product].id] ? $scope.basket[data.results[product].id] : 0;
                        amount += data.results[product].price * quantity;
                    }
                    return amount;

                }, function (val) {
                    $scope.amount = val;
                });

                for (var product in data.results) {
                    $scope.amount += data.results[product].price * $scope.basket[data.results[product].id];
                }
            });
            
            $scope.removeFromCard = function (id) {
                delete $scope.basket[id];
                $scope.empty = Object.keys($scope.basket).length === 0;
                $cookies.putObject('basket', $scope.basket)
            };

            $scope.changeQuantity = function () {
                $cookies.putObject('basket', $scope.basket)
            };

            $scope.clearBasket = function () {
                $scope.empty = true;
                $cookies.remove('basket');
            };

            $scope.showUserPopup = function(){
               $uibModal.open({
                    animation: true,
                    controller: 'confirmOrderCtrl',
                    templateUrl: 'confirm_order/confirm_order.html'
                });
            };
        }
    });
