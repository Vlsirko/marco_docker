'use strict';

angular.module('MirrorStore.confirmOrder', [])

    .controller('confirmOrderCtrl', function ($scope, $uibModalInstance, $cookies, Order, $location, Email, $templateRequest, $compile) {
        $scope.close = $uibModalInstance.close;

        $scope.user = {};
        $scope.comment = '';

        $scope.deliveryMethods = [
            {id: 0, title: 'Самовывоз'},
            {id: 1, title: 'Новая Почта'},
            {id: 2, title: 'Укрпочта'}
        ];

        $scope.defaultMethod = $scope.deliveryMethods[0];

        $scope.confirmOrder = function(){
            Order.save({
                user: $scope.user,
                basket: $cookies.getObject('basket'),
                comment: $scope.comment,
                delivery_method: $scope.defaultMethod.id
            }, function(data){

                $templateRequest('/components/templates/basket_email.html').then(function(template){

                    var body = angular.element('<div></div>');
                    $scope.order = data;
                    console.log(body.append($compile(template)($scope)).html());

                  /*  Email.send({
                        'email': data.user.email,
                        'from': 'MirrorStore',
                        'theme': 'Заказ№' + data.id,
                        'body': $compile(body)($scope).html()
                    });*/
                });



                alert('Заказ успешно оформлен');
                $cookies.remove('basket');
                $uibModalInstance.close();
                $location.hash('basket');
            }, function(){
                alert('error')
            });
        }
    });
