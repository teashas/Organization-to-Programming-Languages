(define mycount
    (lambda (x input)
    (cond ((null? input) 0)
          ((= x (car input)) (+ 1 (mycount x (cdr input))))
          (else (mycount x (cdr input))))))

(define tagmatch 
  (lambda (x input)
    (cond ((null? input) '())
          ((= x (car input)) (cons 1 (tagmatch x (cdr input))))
          (else (cons 0 (tagmatch x (cdr input)))))))
