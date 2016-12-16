
(cl:in-package :asdf)

(defsystem "cup_grabber-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MultiARPose" :depends-on ("_package_MultiARPose"))
    (:file "_package_MultiARPose" :depends-on ("_package"))
    (:file "ARPose" :depends-on ("_package_ARPose"))
    (:file "_package_ARPose" :depends-on ("_package"))
  ))