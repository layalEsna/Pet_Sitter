
import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';


function SignupForm() {

    const formik = useFormik({
        initialValues: {
            user_name: '',
            password: '',
            confirm_password: '',
            
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
        }),
        onSubmit: (values) => {
            fetch('/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(values)
            })
                .then(res => {
                    if (res.ok) {
                        return res.json()
                        // console.log('Successful submit')
                    } else {
                        throw new Error(`Submit failed! ${res.status}`)
                    }
                })
                .then(data =>  console.log(data))
                .catch(e => console.log(`Network or server error: ${e}`))
            
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
                    onBlur={formik.handleBlur}
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
                    onBlur={formik.handleBlur}
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
                    onBlur={formik.handleBlur}
                    value={formik.values.confirm_password}
                    onChange={formik.handleChange}
                />
                <div>
                    {formik.errors.confirm_password && formik.touched.confirm_password && (
                        <div className='error'>{formik.errors.confirm_password}</div>
                    )}
                </div>
            </div>
            
            <div><button type='submit'>Sign Up</button></div>

        </form>
    )
}

export default SignupForm