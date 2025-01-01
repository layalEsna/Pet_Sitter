
import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';


function SignupForm() {

    const formik = useFormik({
        initialValues: {
            user_name: '',
            password: '',
            confirm_password: '',
            // pet_name: '',
            // pet_type: '',
            // zip_code: '',
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
            // pet_name: Yup.string()
            //     .required('Pet name is required'),
            // pet_type: Yup.string()
            //     .required('Pet type is required.'),
            // zip_code: Yup.string()
            //     .matches(/^\d{5}$/, 'Zip code must be a valid 5-digit number')
            //     .required('Zip code is requied')
        }),
        onSubmit: (values) => {
            console.log(`Form data: ${values}`)
        }
    })

    return (
        <form onSubmit={formik.handleSubmit}>
            <div>
                <label htmlFor='user_name'>Create username</label>
                <input
                    id='user_name'
                    type='text'
                    name='user_name'
                    value={formik.values.user_name}
                    onChange={formik.handleChange}
                />
                {formik.errors.user_name && formik.touched.user_name && (
                    <div className='error'>{formik.errors.user_name}</div>
                )}
            </div>
            <br />
            <div>
                <label htmlFor='password'>Create password</label>
                <input
                    id='password'
                    type='password'
                    name='password'
                    value={formik.values.password}
                    onChange={formik.handleChange}
                />
                <div>
                    {formik.errors.password && formik.touched.password && (
                        <div className='error'>{formik.errors.password}</div>
                    )}
                </div>
            </div>
            <br />
            <div>
                <label htmlFor='confirm_password'>Confirm password</label>
                <input
                    id='confirm_password'
                    type='password'
                    name='confirm_password'
                    value={formik.values.confirm_password}
                    onChange={formik.handleChange}
                />
                <div>
                    {formik.errors.confirm_password && formik.touched.confirm_password && (
                        <div className='error'>{formik.errors.confirm_password}</div>
                    )}
                </div>
            </div>
            {/* <br /> */}
            {/* <div>
                <label htmlFor='pet_name'>Pet name</label>
                <input
                    id='pet_name'
                    name='pet_name'
                    type='text'
                    value={formik.values.pet_name}
                    onChange={formik.handleChange}
                />
            </div> */}

            {/* <div>
                {formik.errors.pet_name && formik.touched.pet_name && (
                    <div className='error'>{formik.errors.pet_name}</div>
                )}
            </div>
            <br />
            <div>
                <label htmlFor='pet_type'>Pet Type</label>
                <div>
                    <select
                        id='pet_type'
                        name='pet_type'
                        value={formik.values.pet_type}
                        onChange={formik.handleChange}>

                        <option value=''>Select one</option>
                        <option value='cat'>Cat</option>
                        <option value='dog'>Dog</option>
                        <option value='bird'>Bird</option>

                    </select>
                </div>
                <div>
                    {formik.errors.pet_type && formik.touched.pet_type && (
                        <div className='error'>{formik.errors.pet_type}</div>
                    )}
                </div>


            </div> */}
            <br />
            {/* <div>
                <label htmlFor='zip_code'>Zip code</label>
                <input
                    id='zip_code'
                    name='zip_code'
                    type='text'
                    value={formik.values.zip_code}
                    onChange={formik.handleChange}
                />
            </div>
            <div>
                {formik.errors.zip_code && formik.touched.zip_code && (
                    <div className='error'>{formik.errors.zip_code}</div>
                )}
            </div>
            <br /> */}
            <div><button type='submit'>Sign Up</button></div>

        </form>
    )
}

export default SignupForm