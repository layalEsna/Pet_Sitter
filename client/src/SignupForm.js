
import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';


function SignupForm() {

    const formik = useFormik({
        initialValues: {
          user_name: '',
          password: '',
          confirm_password: '',
          pet_name: '',
          pet_type: '',
          zip_code: '',
        },
        validationSchema: Yup.object({
            user_name: Yup.string()
                .min(3, 'Username must be at least 3 characters.')
                .required('Username is required.'),
            password: Yup.string()
                .min(8, 'Password must be at least 8 characters')
                .required('Password is required.'),
            confirm_password: Yup.string()
                .oneOf([Yup.ref('password'), null], 'Password must match')
                .required('Confirm password is required.'),
            pet_name: Yup.string()
                .required('Pet name is required'),
            pet_type: Yup.string()
                .required('Pet type is required.'),
            zip_code: Yup.string()
                .matches(/^\d{5}$/, 'Zip code must be a valid 5-digit number')
                .required('Zip code is requied')
             })
    })
    
    



    


}

export default SignupForm