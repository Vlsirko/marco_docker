'use strict';

angular.module('MirrorStore')
    .directive('rsSlider', [function () {
        return {
            'link': function (scope, elem, attrs) {

                if (scope.$last) {
                    $(elem.parent()).responsiveSlides({
                        auto: true,
                        pager: true,
                        nav: true,
                        speed: 1000,
                        namespace: "centered-btns"
                    });

                }
            }
        };
    }])
    .directive('scrollOnClick', function () {
        return {
            restrict: 'A',
            link: function (scope, $elm) {
                $elm.on('click', function () {
                    $("body").animate({scrollTop: 0}, "slow");
                });
            }
        }
    })
    .directive('marcoPagination', ['$location', '$window', function ($location, $window) {
        return {
            restrict: 'E',
            templateUrl: '/components/templates/pagination.html',
            link: function ($scope, element, attrs) {
                var SHOW_PAGES = 11;

                attrs.$observe('page', function (page) {
                    page = eval(page);
                    var currPage = page[0];
                    var pagesCount = page[1];

                    $scope.pages = [];
                    if (pagesCount == 1) {
                        return;
                    }

                    if (pagesCount <= SHOW_PAGES) {
                        for (var i = 1; i <= pagesCount; i++) {
                            $scope.pages.push(i);
                        }
                    } else {
                        var leftRange = [1, SHOW_PAGES - 2];
                        var rightRange = [pagesCount - (SHOW_PAGES - 2), pagesCount];

                        if (currPage >= leftRange[0] && currPage < leftRange[1]) {

                            for (var i = leftRange[0]; i <= leftRange[1]; i++) {
                                $scope.pages.push(i)
                            }
                            $scope.pages.push('...');
                            $scope.pages.push(pagesCount);

                        } else if (currPage > rightRange[0] && currPage <= rightRange[1]) {

                            $scope.pages.push(1);
                            $scope.pages.push('...');
                            for (var i = rightRange[0]; i <= rightRange[1]; i++) {
                                $scope.pages.push(i)
                            }

                        } else {
                            $scope.pages.push(1);
                            $scope.pages.push('...');
                            var delta = parseInt((SHOW_PAGES - 4) / 2);
                            var centerRange = [currPage - delta, currPage + delta];
                            console.log(centerRange);
                            for (var i = centerRange[0]; i <= centerRange[1]; i++) {
                                $scope.pages.push(i)
                            }

                            $scope.pages.push('...');
                            $scope.pages.push(pagesCount);
                        }
                    }

                });


                //console.log(pagesCount);

                $scope.changePage = function (page) {
                    $location.search(
                        angular.extend(
                            $location.search(),
                            {page: page}
                        )
                    );
                    $window.scrollTo(0, 0);
                }
            }
        }
    }]);