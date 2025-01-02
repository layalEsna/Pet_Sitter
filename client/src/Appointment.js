import { useFormik } from 'formik';
import * as Yup from 'yup';

function Appointment() {

    const appointmentForm = useFormik({
        initialValues: {
            pet_name: '',
            pet_type: '',
            date: '',
            duration: ''
        },
        validationSchema: Yup.object({
            pet_name: Yup.string(),
            pet_type: Yup.string()
                .required('Pet type is required.'),
            date: Yup.string()
                .required('Date is required')
                .test(
                    'is-future',
                    'Date must be in the future.',

                    (value) => {
                        if (!value) return false
                        const today = new Date()
                        
                        const inputDate = new Date(value)
                        
                        return inputDate >= today
                        
                }

            ),
            
            duration: Yup.number()
                .required('Duration is required.')
        }),
        onSubmit: (values) => {
            console.log(`Form submitted, ${values}`)
        }
    })
    return (
        <div>
            <h1>Appointment Form</h1>

            <form onSubmit={appointmentForm.handleSubmit}>
                <div>
                    <label htmlFor='pet_name'>Pet name</label>
                    <input
                        id='pet_name'
                        name='pet_name'
                        type='text'
                        value={appointmentForm.values.pet_name}
                        onBlur={appointmentForm.handleBlur}
                        onChange={appointmentForm.handleChange}
                    />
                    {appointmentForm.touched.pet_name && appointmentForm.errors.pet_name ? (
                        <div className='error'>{appointmentForm.errors.pet_name}</div>
                    ) : null}
                </div>
                <br />
                <div>
                    <label htmlFor='pet_type'>Pet type</label>
                    <select
                        id='pet_type'
                        name='pet_type'
                        onBlur={appointmentForm.handleBlur}
                        onChange={appointmentForm.handleChange}
                        value={appointmentForm.values.pet_type}
                    >
                        <option value=''>select a type</option>
                        <option value='cat'>Cat</option>
                        <option value='dog'>Dog</option>
                        <option value='bird'>Bird</option>
                    </select>
                    {appointmentForm.touched.pet_type && appointmentForm.errors.pet_type ? (
                        <div className='error'>{appointmentForm.errors.pet_type}</div>
                    ) : null}
                </div>
                <br />
                <div>
                    <label htmlFor='date'>Date: yyyy-dd-mm</label>
                    <input
                        id='date'
                        name='date'
                        type='date'
                        value={appointmentForm.values.date}
                        onBlur={appointmentForm.handleBlur}
                        onChange={appointmentForm.handleChange}
                    />
                    {appointmentForm.touched.date && appointmentForm.errors.date ? (
                        <div className='error'>{appointmentForm.errors.date}</div>
                    ) : null}
                </div>
                <br />
                <div>
                    <label htmlFor='duration'>Duration</label>
                    <select
                        id='duration'
                        name='duration'
                        value={appointmentForm.values.duration}
                        onBlur={appointmentForm.handleBlur}
                        onChange={appointmentForm.handleChange}
                    >
                        <option value=''>Number of days</option>
                        <option value='1'>1 day</option>
                        <option value='2'>2 days</option>
                        <option value='3'>3 days</option>
                        <option value='4'>4 days</option>
                        <option value='5'>5 days</option>
                        <option value='6'>6 days</option>
                        <option value='7'>7 days</option>
                        <option value='8'>8 days</option>
                        <option value='9'>9 days</option>
                        <option value='10'>10 days</option>

                    </select>
                    {appointmentForm.touched.duration && appointmentForm.errors.duration ? (
                        <div className='error'>{appointmentForm.errors.duration}</div>
                    ) : null}
                </div>
                <button onSubmit={appointmentForm.handleSubmit}>Submit</button>

            </form>

        </div>
    )


}


export default Appointment