'use strict';

angular.module('MirrorStore.confirmOrder', [])

    .controller('confirmOrderCtrl', function ($scope, $uibModalInstance, $cookies, Order, $location, Email, $templateRequest, $compile, $timeout, MirrorStoreConfig) {
        $scope.close = $uibModalInstance.close;

        $scope.user = {};
        $scope.comment = '';

        $scope.deliveryMethods = [
            {id: 0, title: 'Самовывоз'},
            {id: 1, title: 'Новая Почта'},
            {id: 2, title: 'Укрпочта'}
        ];

        $scope.defaultMethod = $scope.deliveryMethods[0];

        $scope.confirmOrder = function () {
            Order.save({
                user: $scope.user,
                basket: $cookies.getObject('basket'),
                comment: $scope.comment,
                delivery_method: $scope.defaultMethod.id
            }, function (data) {

                $templateRequest('/components/templates/basket_email.html').then(function (template) {
                    $scope.order = data;
                    $scope.site = MirrorStoreConfig.site;
                    var compiled = $compile(template)($scope);
                    $timeout(function(){

                        Email.send({
                            'email': [data.user.email].concat(MirrorStoreConfig.emails.admins),
                            'from': MirrorStoreConfig.emails.from,
                            'theme': 'Заказ№' + data.id,
                            'body': compiled[0].outerHTML
                        });

                        alert('Заказ успешно оформлен');
                        $cookies.remove('basket');
                        $uibModalInstance.close();
                        $location.hash('basket');

                    }, 300)

                });



            }, function () {
                alert('error')
            });
        }
    });
