'use strict';

angular.module('MirrorStore.confirmOrder', [])

    .controller('confirmOrderCtrl', function ($scope, $uibModalInstance, $cookies, Order, $location) {
        $scope.close = $uibModalInstance.close;

        $scope.user = {};
        $scope.comment = '';

        $scope.deliveryMethods = [
            'Самовывоз', 'Новая Почта', 'Укрпочта'
        ];

        $scope.defaultMethod = 0;

        $scope.confirmOrder = function(){
            Order.save({
                user: $scope.user,
                basket: $cookies.getObject('basket'),
                comment: $scope.comment,
                delivery_method: $scope.delivery_method
            }, function(){
                alert('Заказ успешно оформлен');
                $cookies.remove('basket');
                $uibModalInstance.close();
                $location.hash('basket');
            }, function(){
                alert('error')
            });
        }
    });
